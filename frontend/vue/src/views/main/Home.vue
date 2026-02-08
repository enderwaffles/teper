<template>
  <h1>Home</h1>
  <p>{{ message }}</p>
</template>

<script setup>

import { ref, onMounted } from "vue";

const message = ref("");

async function loadMessage() {
  try {
    const res = await fetch("http://localhost:8000/");
    const data = await res.json();

    message.value = data.message;
  } 
  catch {
    message.value = "Error";
  }
}

loadMessage();

</script>
