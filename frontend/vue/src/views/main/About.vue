<template>
  <h1>About</h1>
  <p>{{ message }}</p>
</template>

<script setup>

import { ref, onMounted } from "vue";

const message = ref("");

async function loadMessage() {
  try {
    const response = await fetch("http://localhost:8000/about");
    const data = await response.json();

    message.value = data.message;
  } 
  catch {
    message.value = "Error";
  }
}

loadMessage();

</script>
