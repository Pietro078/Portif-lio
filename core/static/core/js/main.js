document.addEventListener("DOMContentLoaded", () => {
  const terminalLines = [
    "$ python disparo_relatorios.py",
    "> conectando ao servidor de e-mail...",
    "> gerando relatorio_vendas.xlsx",
    "> destinatarios: 12 encontrados",
    "> enviando relatorios...",
    "✓ envio concluido com sucesso",
  ];

  const terminalEl = document.getElementById("terminalBody");
  if (terminalEl) {
    typeTerminalLines(terminalEl, terminalLines);
  }

  const navToggle = document.getElementById("navToggle");
  const nav = document.getElementById("siteNav");
  if (navToggle && nav) {
    navToggle.addEventListener("click", () => {
      const isOpen = nav.classList.toggle("nav-open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        nav.classList.remove("nav-open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }
});

function typeTerminalLines(target, lines, lineIndex = 0, charIndex = 0) {
  if (lineIndex >= lines.length) {
    setTimeout(() => {
      target.textContent = "";
      typeTerminalLines(target, lines, 0, 0);
    }, 2200);
    return;
  }

  const currentLine = lines[lineIndex];
  const previousLines = lines.slice(0, lineIndex).join("\n");
  target.textContent =
    (lineIndex > 0 ? previousLines + "\n" : "") + currentLine.slice(0, charIndex);

  if (charIndex < currentLine.length) {
    setTimeout(() => typeTerminalLines(target, lines, lineIndex, charIndex + 1), 28);
  } else {
    setTimeout(() => typeTerminalLines(target, lines, lineIndex + 1, 0), 350);
  }
}
