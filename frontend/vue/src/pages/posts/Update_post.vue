<template>
  <Header />

  <div>
    <h1>Update post</h1>
  </div>

  <div>
    
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

//functions

</script>


<style scoped>

</style>
