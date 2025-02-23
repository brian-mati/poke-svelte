<script lang="ts">
let search:String = $props()
</script>

<input type="text" class="border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
    placeholder="Search" bind:value={search} />