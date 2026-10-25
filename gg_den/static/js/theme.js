(() => {
  const root = document.documentElement;
  const key = "gg-den-theme";
  const saved = localStorage.getItem(key);
  if (saved === "light" || saved === "dark") root.dataset.theme = saved;
  const button = document.getElementById("themeToggle");
  if (button) {
    const update = () => { button.textContent = root.dataset.theme === "dark" ? "☼ Sáng" : "☾ Tối"; };
    update();
    button.addEventListener("click", () => {
      root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
      localStorage.setItem(key, root.dataset.theme);
      update();
    });
  }
})();
