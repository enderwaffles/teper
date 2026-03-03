<template>
  <Header />

  <div class="title">
    <h1>Verification</h1>
  </div>

  <div>
    <input type="incode" v-model="incode" placeholder="Code" />

    <button v-on:click="verify">{{ loading ? 'Loading...' : 'Verify' }}</button>
    <p v-if="message">{{ message }}</p>
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
const router = useRouter()
const route = useRoute()


//data
var email = ref(route.query.email || "")
var incode = ref("")

let message = ref("")
let loading = ref(false)


//functions
async function verify() {

  try {
    loading.value = true
    message.value = ""

    const res = await api.post('/verify', {
      email: email.value,
      code: incode.value
    })

    console.log(res)
    if (res.status == 200) {
        auth.login(res.data.user)

        router.push('/')
    }
  }
  catch (error) {
    console.log(error)
    message.value = "Verification failed"
  }
  finally {
    loading.value = false
  }
}

</script>


<style scoped>

</style>
