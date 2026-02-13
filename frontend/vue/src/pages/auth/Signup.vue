<template>
  

      <div class="links">
        <RouterLink to="/login">
          Already have an account?
        </RouterLink>

        <RouterLink to="/">
          ← Back home
        </RouterLink>
      </div>

</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const router = useRouter()

const name = ref('')
const password = ref('')

async function signup() {
  if (!name.value || !password.value) {
    alert('Fill all fields')
    return
  }

  try {
    await api.post('/signup', {
      name: name.value,
      password: password.value
    })

    router.push('/login')
  } catch (err) {
    alert('Signup failed')
  }
}
</script>

<style scoped>

</style>
