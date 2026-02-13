<template>
<h1>Signup</h1>

<input type="text" v-model="email" placeholder="email">
<input type="text" v-model="nickname" placeholder="nickname">
<input type="text" v-model="name" placeholder="name">
<input type="text" v-model="surname" placeholder="surname">
<input type="text" v-model="password" placeholder="password">
<input type="text" v-model="repeat_password" placeholder="repeat_password">
<button type="button" v-on:click="signup()">Signup</button>
<p>{{ message }}</p>
<RouterLink to="/login">Already have an account? </RouterLink>
<RouterLink to="/">Back to home </RouterLink>

</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const router = useRouter()

const email = ref("")
const nickname = ref("")
const name = ref("")
const surname = ref("")
const password = ref("")
const repeat_password = ref("")

const message = ref("")

async function signup() {
  // if (!email.value || !nickname.value || !name.value || !surname.value || !password.value || !repeat_password.value) {
  //   alert("Fill all fields")
  //   return
  // }
  // if (password.value != repeat_password.value) {
  //   alert("Passwords dont match")
  //   return
  // }

  try {
    await api.post('/signup', {
      email: email.value,
      nickname: nickname.value,
      name: name.value,
      surname: name.value,
      password: password.value
    })

    router.push('/login')
  }
  catch (error) {
    console.log(error)
    message.value = error
  }
}
</script>

<style scoped></style>
