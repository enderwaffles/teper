<template>
  <RouterView />
</template>

<script setup>
</script>

<style>
/* ===== GLOBAL RESET ===== */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* ===== BASE ===== */
body {
  /* font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; */

  background: #111; /* темный приятный фон */
  color: #e2e8f0;      /* мягкий белый */
}

/* Ссылки по умолчанию */
a {
  color: #94a3b8;
  text-decoration: none;
  transition: 0.2s;
}

a:hover {
  color: white;
}

/* Чтобы inputs/buttons не выглядели по-разному на разных браузерах */
input, button {
  font: inherit;
}
</style>
