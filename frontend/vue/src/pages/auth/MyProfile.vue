<template>
  <Header />

  <div>
    <h1>Profile</h1>
  </div>

  <div>
    <p><b>Email:</b> {{ auth.user?.email }}</p>
    <p><b>Nickname:</b> {{ auth.user?.nickname }}</p>
    <p><b>Name:</b> {{ auth.user?.name }}</p>
    <p><b>Surname:</b> {{ auth.user?.surname }}</p>

    <p v-if="auth.user.admin" style="color: red;">You are admin</p>
    <button v-on:click="logout">Logout</button>
  </div>

</template>


<script setup>
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()


//data



//functions
function logout() {
  auth.logout()
  router.push('/')
}

</script>

<style scoped>

</style>
