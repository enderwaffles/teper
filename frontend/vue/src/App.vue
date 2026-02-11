
<template>

    <User title="hello" @submit="getName"/>
</template>

<script setup>
import User from "./components/Name.vue"

function getName(value) {
    console.log(value)
}

</script>

