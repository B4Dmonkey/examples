<template>
  <!-- <div class="container mx-auto"> -->
  <div class="h-screen grid grid-cols-1 gap-10 content-center">
    <div class="flex justify-center">
      <img src="~/assets/img/logo-no-background.svg" />
    </div>

    <div class="flex justify-center">
      <input type="text" placeholder="Type here" class="input input-bordered w-full max-w-xs" />
    </div>

    <div class="flex justify-center">
      <button class="btn">Login</button>
    </div>
  </div>
  <!-- <Tutorial/> -->
</template>

<script>
export default {
  name: "IndexPage",
};
</script>
