<script setup>
import LoginForm from '../LoginForm.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

function onSuccess() {
  router.push('/') // после логина на главную
}
</script>

<template>
  <div>
    <LoginForm @success="onSuccess" @back="() => {}" />
    <button @click="router.push('/signup')">Go Signup</button>
  </div>
</template>
