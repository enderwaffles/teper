<template>
<p>{{ auth.user }}</p>
<button type="button" v-on:click="logout()">Logout</button>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { useRouter, RouterLink } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

function logout() {
  auth.logout()
  router.push('/')
}
</script>

<style scoped>

</style>
