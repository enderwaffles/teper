<template>
  <Header />
  
  <div>
    <h1>About</h1>
  </div>

  <div>
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


///data
let message = ref("")


//functions
onMounted(async () => {
  try {
    const res = await api.get("/about")
    message.value = res.data.message
  } 
  catch {
    message.value = ""
  }
})

</script>


<style scoped>

</style>
