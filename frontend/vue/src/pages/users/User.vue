<template>
  <Header />

  <div>
    <h1>User</h1>
  </div>

  <div>
    <p><b>Email:</b> {{ user.email }}</p>
    <p><b>Nickname:</b> {{ user.nickname }}</p>
    <p><b>Name:</b> {{ user.name }}</p>
    <p><b>Surname:</b> {{ user.surname }}</p>

    <p v-if="auth.user.admin" style="color: red;">You are admin</p>
    <button v-on:click="logout">Logout</button>
  </div>
  <p>{{ user_nickname }}</p>
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
let user = ref("")
let user_nickname = route.params.nickname

//functions
onMounted(async () => {
    const res = await api.get(`/users/${user_nickname}`)
    user.value = res.data
})

</script>

<style scoped>

</style>
