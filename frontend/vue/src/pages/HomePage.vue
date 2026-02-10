<script setup>
import api from '../api'
import { useRouter } from 'vue-router'

const router = useRouter()

async function logout() {
  await api.post('/logout')
  router.push('/login')
}
</script>

<template>
  <div>
    <p>Home (protected)</p>
    <button @click="router.push('/secret')">Go Secret</button>
    <button @click="logout">Logout</button>
  </div>
</template>
