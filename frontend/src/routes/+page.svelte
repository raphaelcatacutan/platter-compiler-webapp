<script lang="ts">
  // You can add reactive state here later
 export let data: { message: string };
</script>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 4rem;
    font-family: system-ui, sans-serif;
  }

  h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
  }

  p {
    font-size: 1.2rem;
    color: #666;
  }
</style>

<main>
  <h1>Welcome to Platter</h1>
  <p>Your modular compiler playground starts here.</p>
  <p>{data.message}</p>
</main>
