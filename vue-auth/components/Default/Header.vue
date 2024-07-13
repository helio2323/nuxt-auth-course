<template>
    <div>
        <NuxtLink to="/">Home</NuxtLink>
        <NuxtLink to="/about">About</NuxtLink>
        <NuxtLink to="/login">Login</NuxtLink>
    </div>
</template>

<script setup>

</script>

<style  scoped>
div {
    display: flex;
    flex-direction: row;
    gap: 20px;
    justify-content: center;
    padding: 30px;

}

div a {
    color: black;
    text-decoration: none;
    font-size: 20px;
}

div a:hover {
    text-decoration: underline;
    color: blue;
    transition: all 0.3s ease;
    
}
</style>