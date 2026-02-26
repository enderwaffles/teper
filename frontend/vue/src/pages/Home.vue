<template>
  <Header />
  
  <div style="display: flex; justify-content: center; align-items: center;">
    <h1>Home</h1>
  </div>
  
  <div style="display: flex; justify-content: center; align-items: center;">
    <p>{{ message }}</p>
  </div>
  
</template>


<script setup>
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()


//data
let message = ref("")


//functions
onMounted(async () => {
  try {
    const res = await api.get("")
    message.value = res.data.message
  } 
  catch {
    message.value = ""
  }
})

</script>


<style scoped>

</style>
