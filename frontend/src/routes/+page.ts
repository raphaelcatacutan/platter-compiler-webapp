// frontend/src/routes/+page.ts
export async function load() {
  try {
    const res = await fetch('http://localhost:8000');
    const data = await res.json();
    return { message: data.message };
  } catch (error) {
    return { message: 'Backend connection failed' };
  }
}
