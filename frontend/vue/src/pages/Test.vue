
<template>
    <User title="hello" @submit="getName"/>
    <br>
    <RouterLink to="/">Home</RouterLink>

</template>

<script setup>
import User from "../components/Name.vue"

function getName(value) {
    console.log(value)
}

</script>

