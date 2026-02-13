<template>
<h1>Login</h1>

<input type="text" v-model="email" placeholder="email">
<input type="text" v-model="password" placeholder="password">
<button type="button" v-on:click="login()">Login</button>
<p>{{ message }}</p>
<RouterLink to="/signup">Don't have an account? </RouterLink>
<RouterLink to="/">Back to home </RouterLink>

</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const auth = useAuthStore()
const router = useRouter()

const email = ref("")
const password = ref("")

const message = ref("")

const loading = ref(false)

async function login() {

  if (!email.value || !password.value) {
    return
  }

  try {
    loading.value = true

    const res = await api.post('/login', {

      email: email.value,
      password: password.value
    })

    auth.login({
      id: res.data.user.id,
      name: res.data.user.name
    })

    router.push('/')

  } 
  catch (error) {
    console.log(error)
    message.value = error
  }
}
</script>
<style scoped></style>
