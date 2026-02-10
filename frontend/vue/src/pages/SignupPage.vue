<script setup>
import SignupForm from '../SignupForm.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

function onDone() {
  router.push('/login')
}
</script>

<template>
  <div>
    <SignupForm @done="onDone" @back="() => router.push('/login')" />
  </div>
</template>
