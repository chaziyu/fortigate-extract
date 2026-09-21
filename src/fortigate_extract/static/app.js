document.addEventListener("DOMContentLoaded", () => {
  let currentFile = null;
  let sourceReady = false;
  let previewController = null;

  const dropzone = document.getElementById("file-dropzone");
  const fileInput = document.getElementById("file-input");
  const selectedFileCard = document.getElementById("selected-file-card");
  const selectedFilename = document.getElementById("selected-filename");
  const selectedFilesize = document.getElementById("selected-filesize");
  const btnRemoveFile = document.getElementById("btn-remove-file");
  const btnExtractExcel = document.getElementById("btn-extract-excel");
  const previewStatus = document.getElementById("preview-status");
  const inventorySummary = document.getElementById("inventory-summary");
  const errorBanner = document.getElementById("error-message");
  const btnNewWorkspace = document.getElementById("btn-new-workspace");
  const btnToggleTheme = document.getElementById("btn-toggle-theme");
  const themeLabel = document.getElementById("theme-label");
  const toastContainer = document.getElementById("toast-container");

  function formatBytes(bytes) {
    if (!Number.isFinite(bytes) || bytes <= 0) return "0 B";
    const units = ["B", "KB", "MB", "GB"];
    const index = Math.min(
      Math.floor(Math.log(bytes) / Math.log(1024)),
      units.length - 1,
    );
    const value = bytes / 1024 ** index;
    return `${value.toFixed(index === 0 ? 0 : 1)} ${units[index]}`;
  }

  function setText(id, value) {
    const element = document.getElementById(id);
    if (element) element.textContent = String(value);
  }

  function count(value) {
    const parsed = Number(value);
    return Number.isFinite(parsed) && parsed >= 0 ? parsed : 0;
  }

  function showError(message) {
    if (!errorBanner) return;
    errorBanner.textContent = message;
    errorBanner.classList.remove("hidden");
  }

  function hideError() {
    if (!errorBanner) return;
    errorBanner.textContent = "";
    errorBanner.classList.add("hidden");
  }

  function setPreviewStatus(message, state = "idle") {
    if (!previewStatus) return;
    previewStatus.textContent = message;
    previewStatus.dataset.state = state;
    previewStatus.classList.toggle("hidden", !message);
  }

  function setBusy(busy) {
    if (!btnExtractExcel) return;
    btnExtractExcel.disabled = busy || !sourceReady;
    btnExtractExcel.setAttribute("aria-busy", String(busy));
    btnExtractExcel.querySelector(".spinner")?.classList.toggle("hidden", !busy);
    const text = btnExtractExcel.querySelector(".btn-text");
    if (text) {
      text.textContent = busy ? "Building Excel Report..." : "Download Excel Report";
    }
  }

  function resetCounts() {
    [
      "validation-error-count",
      "validation-warning-count",
    ].forEach((id) => setText(id, "—"));

    setText("stat-total-rules", "0");
    setText("stat-total-objects", "0");
    inventorySummary?.classList.add("hidden");
  }

  function clearSource() {
    previewController?.abort();
    previewController = null;
    currentFile = null;
    sourceReady = false;

    if (fileInput) fileInput.value = "";
    selectedFileCard?.classList.add("hidden");
    dropzone?.classList.remove("hidden");
    setPreviewStatus("");
    hideError();
    resetCounts();
    setBusy(false);
  }

  async function readJson(response, fallback) {
    const data = await response.json().catch(() => null);
    if (!response.ok || !data || data.success === false) {
      throw new Error(data?.error || fallback);
    }
    return data;
  }

  async function previewFile(file) {
    previewController?.abort();
    previewController = new AbortController();
    sourceReady = false;
    setBusy(false);
    hideError();
    setPreviewStatus(
      "Reading the FortiGate configuration and preparing the inventory…",
      "loading",
    );

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("/api/preview", {
        method: "POST",
        body: formData,
        signal: previewController.signal,
      });

      const data = await readJson(
        response,
        "Could not read this FortiGate configuration.",
      );

      const objects = data.objects || {};
      const validation = data.validation || {};
      const severity = validation.severity_counts || {};

      const policies = count(objects.policies);
      const addresses = count(objects.addresses);
      const addressGroups = count(objects.address_groups);
      const services = count(objects.services);
      const serviceGroups = count(objects.service_groups);
      const objectTotal =
        addresses + addressGroups + services + serviceGroups;

      setText("validation-error-count", count(severity.error));
      setText("validation-warning-count", count(severity.warning));
      setText("stat-total-rules", policies);
      setText("stat-total-objects", objectTotal);

      inventorySummary?.classList.remove("hidden");
      sourceReady = true;
      setPreviewStatus(
        "Configuration parsed successfully. The Excel report is ready to generate.",
        "ready",
      );
      setBusy(false);
    } catch (error) {
      if (error.name === "AbortError") return;
      sourceReady = false;
      setBusy(false);
      setSummaryState("Review source", "error");
      setPreviewStatus(error.message, "error");
      showError(`Configuration preview failed: ${error.message}`);
    } finally {
      previewController = null;
    }
  }

  function handleFile(file) {
    if (!file) return;

    if (!file.size) {
      showError("The selected configuration file is empty.");
      return;
    }

    currentFile = file;
    sourceReady = false;
    hideError();

    if (selectedFilename) selectedFilename.textContent = file.name;
    if (selectedFilesize) selectedFilesize.textContent = formatBytes(file.size);

    dropzone?.classList.add("hidden");
    selectedFileCard?.classList.remove("hidden");
    previewFile(file);
  }

  async function saveBlob(blob, filename) {
    if (window.pywebview?.api?.save_file_dialog) {
      const buffer = await blob.arrayBuffer();
      const bytes = new Uint8Array(buffer);
      let binary = "";
      const chunkSize = 0x8000;

      for (let offset = 0; offset < bytes.length; offset += chunkSize) {
        binary += String.fromCharCode(
          ...bytes.subarray(offset, offset + chunkSize),
        );
      }

      const result = await window.pywebview.api.save_file_dialog(
        filename,
        btoa(binary),
      );

      return Boolean(result?.success);
    }

    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = filename;
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    return true;
  }

  async function exportExcel() {
    if (!currentFile || !sourceReady) return;

    setBusy(true);
    hideError();

    const formData = new FormData();
    formData.append("file", currentFile);

    try {
      const response = await fetch("/api/extract/excel", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const data = await response.json().catch(() => null);
        throw new Error(data?.error || "Failed to generate the Excel report.");
      }

      const blob = await response.blob();
      const sourceName = currentFile.name.replace(/\.[^.]+$/, "");
      const saved = await saveBlob(
        blob,
        `${sourceName}_fortigate_inventory.xlsx`,
      );

      if (saved) {
        showToast("Excel report generated.");
        setPreviewStatus(
          "Excel report generated successfully.",
          "ready",
        );
      }
    } catch (error) {
      showError(`Excel export failed: ${error.message}`);
      setPreviewStatus(error.message, "error");
    } finally {
      setBusy(false);
    }
  }

  function showToast(message) {
    if (!toastContainer) return;

    const toast = document.createElement("div");
    toast.className = "toast toast-success";
    toast.textContent = message;
    toastContainer.appendChild(toast);

    setTimeout(() => toast.remove(), 3200);
  }

  function preventDefaults(event) {
    event.preventDefault();
    event.stopPropagation();
  }

  if (dropzone && fileInput) {
    ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
      dropzone.addEventListener(eventName, preventDefaults);
    });

    ["dragenter", "dragover"].forEach((eventName) => {
      dropzone.addEventListener(eventName, () => {
        dropzone.classList.add("dragover");
      });
    });

    ["dragleave", "drop"].forEach((eventName) => {
      dropzone.addEventListener(eventName, () => {
        dropzone.classList.remove("dragover");
      });
    });

    dropzone.addEventListener("drop", (event) => {
      const files = event.dataTransfer?.files;
      if (files?.length) handleFile(files[0]);
    });

    dropzone.addEventListener("click", () => fileInput.click());
    dropzone.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        fileInput.click();
      }
    });

    fileInput.addEventListener("change", () => {
      if (fileInput.files?.length) handleFile(fileInput.files[0]);
    });
  }

  btnRemoveFile?.addEventListener("click", (event) => {
    event.stopPropagation();
    clearSource();
  });

  btnNewWorkspace?.addEventListener("click", clearSource);
  btnExtractExcel?.addEventListener("click", exportExcel);

  function syncThemeButton() {
    const theme = document.documentElement.dataset.theme || "light";
    const next = theme === "dark" ? "light" : "dark";
    if (themeLabel) themeLabel.textContent = `${next === "dark" ? "Dark" : "Light"} mode`;
    btnToggleTheme?.setAttribute("aria-pressed", String(theme === "dark"));
  }

  btnToggleTheme?.addEventListener("click", () => {
    const current = document.documentElement.dataset.theme || "light";
    const next = current === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;

    try {
      localStorage.setItem("fwmigrate-theme", next);
    } catch (_) {
      // Storage can be unavailable in privacy-restricted environments.
    }

    syncThemeButton();
  });

  syncThemeButton();
  clearSource();
});
