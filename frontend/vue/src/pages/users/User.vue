<template>
  <Header />

  <div>
    <h1>User</h1>
  </div>

  <div v-if="user">
    <img :src="api.defaults.baseURL + user.avatar_url" alt="" style="width: 300px;"> <br>
    <p><b>Email:</b> {{ user.email }}</p>
    <p><b>Nickname:</b> {{ user.nickname }}</p>
    <p><b>Name:</b> {{ user.name }}</p>
    <p><b>Surname:</b> {{ user.surname }}</p>
    <button v-on:click="chat">Chat</button>
    <!-- <RouterLink :to="`/chat/${chat.id}`">Chat</RouterLink> -->
    <hr>
    <h1>Posts</h1>
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
let user_nickname = route.params.nickname

//functions
onMounted(async () => {
    const res = await api.get(`/users/${user_nickname}`)
    user.value = res.data
})

async function chat() {
  console.log("Создаём чат с user id:", user.value.id)
  const res = await api.post(`/chats/${user.value.id}`)
  router.push(`/chat/${res.data.id}`)
  
}

</script>

<style scoped>

</style>
