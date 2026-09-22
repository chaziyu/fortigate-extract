document.addEventListener("DOMContentLoaded", () => {
  let currentFile = null;
  let currentReport = null;
  let activeMode = "report";
  let activeReportSection = "overview";
  let activeObjectSection = "addresses";
  let sourceReady = false;
  let reportController = null;

  const dropzone = document.getElementById("file-dropzone");
  const fileInput = document.getElementById("file-input");
  const selectedFileCard = document.getElementById("selected-file-card");
  const selectedFilename = document.getElementById("selected-filename");
  const selectedFilesize = document.getElementById("selected-filesize");
  const btnRemoveFile = document.getElementById("btn-remove-file");
  const btnExtractExcel = document.getElementById("btn-extract-excel");
  const tabReport = document.getElementById("tab-report");
  const tabExtract = document.getElementById("tab-extract");
  const pageTitle = document.getElementById("page-title");
  const pageDescription = document.getElementById("page-description");
  const excelActionFooter = document.getElementById("excel-action-footer");
  const reportContainer = document.getElementById("report-container");
  const reportOverview = document.getElementById("report-overview");
  const reportData = document.getElementById("report-data");
  const reportSummary = document.getElementById("report-summary");
  const reportFilename = document.getElementById("report-filename");
  const reportVdomSummary = document.getElementById("report-vdom-summary");
  const reportObjectTabs = document.getElementById("report-object-tabs");
  const reportSearch = document.getElementById("report-search");
  const reportVdomFilter = document.getElementById("report-vdom-filter");
  const reportSeverityFilter = document.getElementById("report-severity-filter");
  const reportTableHead = document.getElementById("report-table-head");
  const reportTableBody = document.getElementById("report-table-body");
  const reportEmpty = document.getElementById("report-empty");
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

  const reportColumns = {
    interfaces: [
      ["display_name", "Topology"], ["kind", "Kind"], ["ip", "IP / Remote Gateway"],
      ["role", "Role"], ["parent", "Parent"], ["aggregate", "Aggregate"],
      ["status", "Status"], ["review", "Review"],
    ],
    addresses: [
      ["name", "Name"], ["value", "Value"], ["type", "Type"],
      ["address_family", "Family"], ["associated_interface", "Interface"],
      ["review", "Review"],
    ],
    address_groups: [
      ["name", "Name"], ["members", "Members"], ["address_family", "Family"],
      ["exclude_members", "Excluded"], ["review", "Review"],
    ],
    services: [
      ["name", "Name"], ["protocol", "Protocol"], ["port", "Port"],
      ["source_port", "Source Port"], ["generated", "Generated"],
      ["review", "Review"],
    ],
    service_groups: [
      ["name", "Name"], ["members", "Members"], ["generated", "Generated"],
      ["review", "Review"],
    ],
    policies: [
      ["policy_id", "ID"], ["name", "Name"], ["source_interfaces", "Source"],
      ["destination_interfaces", "Destination"], ["services", "Service"],
      ["action", "Action"], ["nat", "NAT"], ["review", "Review"],
    ],
    nat: [
      ["policy_id", "Policy ID"], ["policy_name", "Policy"],
      ["translation_type", "Type"], ["translated_addresses", "Address"],
      ["egress_interfaces", "Egress"], ["review", "Review"],
    ],
    routes: [
      ["route_id", "ID"], ["destination", "Destination"], ["gateway", "Gateway"],
      ["device", "Device"], ["distance", "Distance"], ["status", "Status"],
      ["review", "Review"],
    ],
    vpn: [
      ["kind", "Type"], ["name", "Name"], ["attachment", "Interface / Phase 1"],
      ["peer", "Gateway / Selectors"], ["crypto", "IKE / Proposal"],
      ["topology", "Topology"], ["review", "Review"],
    ],
    validation: [
      ["severity", "Severity"], ["domain", "Domain"], ["object_name", "Object"],
      ["field", "Field"], ["message", "Issue"],
    ],
  };

  function formatCell(value) {
    if (value === null || value === undefined || value === "") return "—";
    if (Array.isArray(value)) return value.length ? value.join(", ") : "—";
    if (typeof value === "boolean") return value ? "Yes" : "No";
    return String(value);
  }

  function reportRows(section) {
    const sections = currentReport?.sections || {};
    if (section === "interfaces") {
      return sections.interface_topology || sections.interfaces || [];
    }
    if (section === "objects") return sections[activeObjectSection] || [];
    if (section === "vpn") {
      return [
        ...(sections.vpn_tunnels || []).map((row) => ({
          ...row,
          kind: "Tunnel",
          attachment: row.interface,
          peer: row.remote_gateway,
          crypto: row.ike_version,
          topology: row.topology_path,
        })),
        ...(sections.vpn_phase2 || []).map((row) => ({
          ...row,
          kind: "Phase 2",
          attachment: row.phase1,
          peer: [row.source_range, row.destination_range].filter(Boolean).join(" → "),
          crypto: row.proposal,
          topology: [],
        })),
      ];
    }
    if (section === "validation") {
      return sections.validation || [];
    }
    return sections[section] || [];
  }

  function renderTable() {
    if (!currentReport || activeReportSection === "overview") return;
    const columnKey = activeReportSection === "objects"
      ? activeObjectSection
      : activeReportSection;
    const columns = reportColumns[columnKey] || [];
    const search = reportSearch?.value.trim().toLowerCase() || "";
    const vdom = reportVdomFilter?.value || "";
    const severity = reportSeverityFilter?.value || "";
    const rows = reportRows(activeReportSection).filter((row) => {
      if (vdom && row.vdom !== vdom) return false;
      if (severity && row.severity !== severity) return false;
      return !search || Object.values(row).some((value) =>
        formatCell(value).toLowerCase().includes(search));
    });

    const headRow = document.createElement("tr");
    columns.forEach(([, label]) => {
      const th = document.createElement("th");
      th.scope = "col";
      th.textContent = label;
      headRow.appendChild(th);
    });
    reportTableHead?.replaceChildren(headRow);

    const fragment = document.createDocumentFragment();
    rows.forEach((row) => {
      const tr = document.createElement("tr");
      columns.forEach(([key]) => {
        const td = document.createElement("td");
        td.textContent = formatCell(row[key]);
        if (columnKey === "interfaces" && key === "display_name") {
          td.className = "report-topology-name";
        }
        tr.appendChild(td);
      });
      fragment.appendChild(tr);
    });
    reportTableBody?.replaceChildren(fragment);
    reportEmpty?.classList.toggle("hidden", rows.length > 0);
  }

  function renderOverview() {
    if (!currentReport || !reportSummary) return;
    const summary = currentReport.summary || {};
    const objects = summary.objects || {};
    const severity = summary.validation?.severity_counts || {};
    const objectTotal = count(objects.addresses) + count(objects.address_groups)
      + count(objects.services) + count(objects.service_groups);
    const stats = [
      ["Interfaces", objects.interfaces], ["Policies", objects.policies],
      ["Objects", objectTotal], ["Errors", severity.error],
      ["Warnings", severity.warning],
    ];
    const fragment = document.createDocumentFragment();
    stats.forEach(([label, value]) => {
      const stat = document.createElement("div");
      stat.className = "report-stat";
      const number = document.createElement("strong");
      number.textContent = String(count(value));
      const caption = document.createElement("span");
      caption.textContent = label;
      stat.append(number, caption);
      fragment.appendChild(stat);
    });
    reportSummary.replaceChildren(fragment);
    if (reportFilename) reportFilename.textContent = currentReport.filename || "";
    if (reportVdomSummary) {
      const vdoms = summary.vdoms || [];
      reportVdomSummary.textContent = vdoms.length
        ? `VDOMs: ${vdoms.join(", ")}`
        : "No VDOM data found.";
    }
  }

  function setReportSection(section) {
    activeReportSection = section;
    document.querySelectorAll("[data-report-section]").forEach((button) => {
      button.classList.toggle("active", button.dataset.reportSection === section);
    });
    const overview = section === "overview";
    reportOverview?.classList.toggle("hidden", !overview);
    reportData?.classList.toggle("hidden", overview);
    reportObjectTabs?.classList.toggle("hidden", section !== "objects");
    reportSeverityFilter?.classList.toggle("hidden", section !== "validation");
    if (!overview) renderTable();
  }

  function renderReport() {
    renderOverview();
    if (reportVdomFilter) {
      reportVdomFilter.replaceChildren();
      const all = document.createElement("option");
      all.value = "";
      all.textContent = "All VDOMs";
      reportVdomFilter.appendChild(all);
      (currentReport?.summary?.vdoms || []).forEach((vdom) => {
        const option = document.createElement("option");
        option.value = vdom;
        option.textContent = vdom;
        reportVdomFilter.appendChild(option);
      });
    }
    setReportSection(activeReportSection);
  }

  function setMode(mode) {
    activeMode = mode;
    const showingReport = mode === "report";
    tabReport?.classList.toggle("active", showingReport);
    tabExtract?.classList.toggle("active", !showingReport);
    tabReport?.toggleAttribute("aria-current", showingReport);
    tabExtract?.toggleAttribute("aria-current", !showingReport);
    excelActionFooter?.classList.toggle("hidden", showingReport);
    reportContainer?.classList.toggle("hidden", !showingReport || !currentReport);

    if (pageTitle) {
      pageTitle.textContent = showingReport
        ? "FortiGate Configuration Report"
        : "Export FortiGate Report";
    }
    if (pageDescription) {
      pageDescription.textContent = showingReport
        ? "Upload a FortiGate CLI backup and review the extracted configuration."
        : "Upload once, then download the complete Excel workbook.";
    }
  }

  function clearSource() {
    reportController?.abort();
    reportController = null;
    currentFile = null;
    currentReport = null;
    sourceReady = false;

    if (fileInput) fileInput.value = "";
    selectedFileCard?.classList.add("hidden");
    dropzone?.classList.remove("hidden");
    setPreviewStatus("");
    hideError();
    resetCounts();
    reportContainer?.classList.add("hidden");
    if (reportSearch) reportSearch.value = "";
    if (reportVdomFilter) reportVdomFilter.value = "";
    if (reportSeverityFilter) reportSeverityFilter.value = "";
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
    reportController?.abort();
    const controller = new AbortController();
    reportController = controller;
    sourceReady = false;
    currentReport = null;
    setBusy(false);
    hideError();
    setPreviewStatus(
      "Reading the FortiGate configuration and preparing the inventory…",
      "loading",
    );

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("/api/report", {
        method: "POST",
        body: formData,
        signal: controller.signal,
      });

      const data = await readJson(
        response,
        "Could not read this FortiGate configuration.",
      );

      const summary = data.summary || {};
      const objects = summary.objects || {};
      const validation = summary.validation || {};
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
      currentReport = data;
      sourceReady = true;
      renderReport();
      setMode(activeMode);
      setPreviewStatus(
        "Configuration parsed successfully. The report is ready.",
        "ready",
      );
      setBusy(false);
    } catch (error) {
      if (error.name === "AbortError") return;
      sourceReady = false;
      currentReport = null;
      setBusy(false);
      setPreviewStatus(error.message, "error");
      showError(`Configuration report failed: ${error.message}`);
    } finally {
      if (reportController === controller) reportController = null;
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
  tabReport?.addEventListener("click", () => setMode("report"));
  tabExtract?.addEventListener("click", () => setMode("excel"));
  document.querySelectorAll("[data-report-section]").forEach((button) => {
    button.addEventListener("click", () => setReportSection(button.dataset.reportSection));
  });
  document.querySelectorAll("[data-object-section]").forEach((button) => {
    button.addEventListener("click", () => {
      activeObjectSection = button.dataset.objectSection;
      document.querySelectorAll("[data-object-section]").forEach((item) => {
        item.classList.toggle("active", item === button);
      });
      renderTable();
    });
  });
  reportSearch?.addEventListener("input", renderTable);
  reportVdomFilter?.addEventListener("change", renderTable);
  reportSeverityFilter?.addEventListener("change", renderTable);

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
  setMode("report");
});
