<template>
<h1>Login</h1>
<input type="text" v-model="name" placeholder="name"> <br>
<input type="text" v-model="password" placeholder="password"> <br>
<button type="button" v-on:click="login()">Login</button> <br>
<RouterLink to="/signup">Don't you have an account?</RouterLink> <br>
<RouterLink to="/">Back home</RouterLink>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

const name = ref("");
const password = ref("");

function login() {
    auth.login({name: name.value, password: password.value});
    router.push("/")
}
</script>
