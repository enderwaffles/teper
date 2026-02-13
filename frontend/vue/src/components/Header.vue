<template>
<header class="header">

<h1>Forgeswords</h1>

<RouterLink class="nav-link" to="/">Home </RouterLink>
<RouterLink class="nav-link" to="/about">About </RouterLink>
<RouterLink class="nav-link" to="/posts">Posts </RouterLink>

<RouterLink v-if="auth.session" to="/create_post">Create post </RouterLink>

<div v-if="!auth.session">
    <RouterLink class="auth-link signup-btn" to="/signup">Sign up </RouterLink>
    <RouterLink class="auth-link" to="/login">Login </RouterLink>
</div>

<div v-else>
    <RouterLink class="auth-link" to="/profile">Profile</RouterLink>
</div>

</header>

</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
const auth = useAuthStore()
</script>

<style scoped>

</style>
