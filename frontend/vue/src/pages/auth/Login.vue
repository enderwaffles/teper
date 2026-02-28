<template>
  <Header />

  <div>
    <h1>Login</h1>
  </div>

  <div>
    <input type="email" v-model="email" placeholder="Email" /> <br>
    <input type="password" v-model="password" placeholder="Password" /> <br>

    <button v-on:click="login">{{ loading ? 'Loading...' : 'Login' }}</button> <br>
    <RouterLink to="/forgot1">Forget password?</RouterLink> <br>
    <p v-if="message">{{ message }}</p>
    <RouterLink to="/signup">Don't have an account?</RouterLink> <br>
    <RouterLink to="/">Back to home</RouterLink>
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
const route = useRoute()
const router = useRouter()


//data
var email = ref("")
var password = ref("")

let message = ref("")
let loading = ref(false)


//functions
async function login() {

  try {
    loading.value = true
    message.value = ""

    const res = await api.post('/login', {
      email: email.value,
      password: password.value
    })

    console.log(res)
    if (res.status == 200) {
        auth.login({
            id: res.data.user.id,
            email: res.data.user.email,
            nickname: res.data.user.nickname,
            name: res.data.user.name,
            surname: res.data.user.surname,
            admin: res.data.user.admin
        })

        router.push('/')
    }
  }
  catch (error) {
    console.log(error)
    message.value = "Login failed"
  }
  finally {
    loading.value = false
  }
}

</script>


<style scoped>

</style>
