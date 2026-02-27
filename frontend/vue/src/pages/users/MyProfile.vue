<template>
  <Header />

  <div>
    <h1>My profile</h1>
  </div>

  <div v-if="user">
    <img :src="api.defaults.baseURL + user.avatar_url" alt="" style="width: 300px;">
    <p><b>Email:</b> {{ user.email }}</p>
    <p><b>Nickname:</b> {{ user.nickname }}</p>
    <p><b>Name:</b> {{ user.name }}</p>
    <p><b>Surname:</b> {{ user.surname }}</p>

    <p v-if="auth.user.admin" style="color: red;">You are admin</p>
    <button v-on:click="logout">Logout</button>
  </div>

</template>


<script setup>
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()


//data
let user = ref(null)


//functions
onMounted(async () => {
  const res = await api.get(`/users/${auth.user.nickname}`)
  user.value = res.data
})

function logout() {
  auth.logout()
  router.push('/')
}

</script>

<style scoped>

</style>
