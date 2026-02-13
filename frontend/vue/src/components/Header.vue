<template>
    <header class="header">

        <!-- Лого -->
        <div class="logo">
            <h1>Forgeswords</h1>
        </div>

        <!-- Навигация -->
        <nav class="nav">
            <RouterLink class="nav-link" to="/">Home</RouterLink>
            <RouterLink class="nav-link" to="/about">About</RouterLink>
            <RouterLink class="nav-link" to="/posts">Posts</RouterLink>

            <RouterLink v-if="auth.session" class="nav-link" to="/create_post">
                Create post
            </RouterLink>
        </nav>

        <!-- Авторизация -->
        <div class="auth">
            <template v-if="!auth.session">
                <RouterLink class="auth-link signup-btn" to="/signup">
                    Sign up
                </RouterLink>
                <RouterLink class="auth-link" to="/login">Login</RouterLink>
            </template>

            <template v-else>
                <RouterLink class="auth-link" to="/profile">{{ auth.user.name }}</RouterLink>
            </template>
        </div>

    </header>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
</script>

<style scoped>

</style>
