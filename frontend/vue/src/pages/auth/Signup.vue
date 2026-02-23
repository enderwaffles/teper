<template>
  <Header />

  <div class="title">
    <h1>Signup</h1>
  </div>

  <main class="auth">

    <div class="card">

      <input
        type="email"
        v-model="email"
        placeholder="Email"
      />

      <input
        type="text"
        v-model="nickname"
        placeholder="Nickname"
      />

      <input
        type="text"
        v-model="name"
        placeholder="Name"
      />

      <input
        type="text"
        v-model="surname"
        placeholder="Surname"
      />

      <input
        type="password"
        v-model="password"
        placeholder="Password"
      />

      <input
        type="password"
        v-model="repeat_password"
        placeholder="Repeat password"
      />

      <button
        :disabled="loading"
        @click="signup"
      >
        {{ loading ? 'Loading...' : 'Signup' }}
      </button>

      <p v-if="message" class="error">
        {{ message }}
      </p>

      <div class="links">
        <RouterLink to="/login">
          Already have an account?
        </RouterLink>

        <RouterLink to="/">
          Back to home
        </RouterLink>
      </div>

    </div>

  </main>
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
let email = ref('')
let nickname = ref('')
let name = ref('')
let surname = ref('')
let password = ref('')
let repeat_password = ref('')
let message = ref('')
let loading = ref(false)


//functions
async function signup() {

  if (
    !email.value ||
    !nickname.value ||
    !name.value ||
    !surname.value ||
    !password.value ||
    !repeat_password.value
  ) {
    message.value = 'Fill in all fields'
    return
  }

  if (password.value !== repeat_password.value) {
    message.value = 'Passwords do not match'
    return
  }

  try {
    loading.value = true
    message.value = ''

    await api.post('/signup', {
      email: email.value,
      nickname: nickname.value,
      name: name.value,
      surname: surname.value,
      password: password.value
    })

    router.push(`/verify?email=${email.value}`)

  }
  catch (error) {
    console.log(error)
    message.value = 'Signup failed'
  }
  finally {
    loading.value = false
  }
}
</script>


<style scoped>

</style>
