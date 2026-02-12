<template>
    <h1>Header</h1>
    <div v-if="!auth.session">     
        <RouterLink to="/signup">Sign up </RouterLink>
        <RouterLink to="/login">Login</RouterLink>
        <br>
    </div> 
    <div v-if="auth.session">
        <!-- <RouterLink to="/">Logout</RouterLink> -->
        <p>{{ auth.user }}</p>
        <button type="button" v-on:click="logout">Logout</button>
        <br>
    </div>
    <div>
        <RouterLink to="/">Home </RouterLink>
        <RouterLink to="/about">About </RouterLink>
        <RouterLink to="/posts">Posts </RouterLink>
        <RouterLink v-if="auth.session" to="/create_post">Create post</RouterLink>
    </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
const auth = useAuthStore();

function logout() {
    auth.logout();
}

</script>


