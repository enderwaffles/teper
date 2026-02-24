<template>
  <Header />

  <div>
    <h1>Signup</h1>
  </div>

  <div>
    <input type="email" v-model="email" placeholder="Email" />
    <input type="text" v-model="nickname" placeholder="Nickname" />
    <input type="text" v-model="name" placeholder="Name" />
    <input type="text" v-model="surname" placeholder="Surname" />
    <input type="password" v-model="password" placeholder="Password" />
    <input type="password" v-model="repeat_password" placeholder="Repeat password" />

    <button v-click="signup">{{ loading ? 'Loading...' : 'Signup' }}</button>
    <p v-if="message">{{ message }}</p>
    <RouterLink to="/login">Already have an account?</RouterLink>
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
var nickname = ref("")
var name = ref("")
var surname = ref("")
var password = ref("")
var repeat_password = ref("")

let message = ref("")
let loading = ref(false)


//functions
async function signup() {

  if (password.value !== repeat_password.value) {
    message.value = "Passwords do not match"
    return
  }

  try {
    loading.value = true
    message.value = ""

    await api.post('/signup', {
      email: email.value,
      nickname: nickname.value,
      name: name.value,
      surname: surname.value,
      password: password.value,
      admin: res.data.user.admin
    })

    router.push(`/verify?email=${email.value}`)

  }
  catch (error) {
    console.log(error)
    message.value = "Signup failed"
  }
  finally {
    loading.value = false
  }
}

</script>


<style scoped>

</style>
