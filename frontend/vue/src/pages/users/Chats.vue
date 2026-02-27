<template>
  <Header />

  <div>
    <h1>Chats</h1>
  </div>

  <div v-for="chat in chats">
    <RouterLink :to="`/chat/${chat.id}`">
      {{ chat.user1_id == auth.user.id ? chat.user2.email : chat.user1.email }}
    </RouterLink>
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
let chats = ref([])

//functions
onMounted(async () => {
    const res = await api.get('/chats')
    chats.value = res.data
})

</script>

<style scoped>

</style>
