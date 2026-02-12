<template>
<h1>Signup</h1>
<input type="text" v-model="name" placeholder="name"> <br>
<input type="text" v-model="password" placeholder="password"> <br>
<button type="button" v-on:click="signup()">Signup</button> <br>
<RouterLink to="/login">Already have an account?</RouterLink> <br>
<RouterLink to="/">Back home</RouterLink>

</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import api from '@/api/api';

const auth = useAuthStore();
const router = useRouter();

const name = ref("");
const password = ref("");

async function signup() {
    const res = await api.post("/signup", {
        name: name.value, 
        password: password.value
    })
    console.log(res.data)
    // auth.login(res.data);
    router.push("/login")
}
</script>
