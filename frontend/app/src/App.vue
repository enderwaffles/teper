<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const msg = ref("");

onMounted(async () => {
  const res = await axios.get("http://localhost:8000/", {
    withCredentials: true, // важно если будут куки
  });
  msg.value = res.data.message;
});
</script>

<template>
  <h1>{{ msg }}</h1>
</template>
