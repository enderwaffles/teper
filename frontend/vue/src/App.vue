<template>
  <div v-if="route.meta.main !== false">
    <h1>App</h1>
    <router-link to="/">Home </router-link>
    <router-link to="/about">About </router-link>
    <router-link to="/posts">Posts </router-link>
    <!-- <router-link to="/empty">Empty  </router-link> -->
  </div>

  <router-view />
</template>

<script setup>
import { useRoute } from "vue-router";
const route = useRoute();
</script>
