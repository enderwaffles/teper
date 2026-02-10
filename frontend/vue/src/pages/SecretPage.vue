<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
</script>

<template>
  <div>
    <p>Secret page (protected)</p>
    <button @click="router.push('/')">Back Home</button>
  </div>
</template>
