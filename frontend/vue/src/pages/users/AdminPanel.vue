<template>
  <Header />

  <div>
    <h1>Admin panel</h1>
  </div>

  <p>{{ message }}</p>

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
let message = ref("")
console.log(message)

//functions
onMounted(async () => {
    try {
        const res = await api.get("admin_panel")
        message.value = res.data.message
    }
    catch(error) {
        message.value = error.response
    }
})


</script>

<style scoped>

</style>
