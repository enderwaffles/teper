<template>
  <Header />

  <div>
    <h1>Chats</h1>
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

//functions
onMounted(async () => {
    // const res = await api.get(`/users/${user_nickname}`)
    // user.value = res.data
})

</script>

<style scoped>

</style>
