<script lang="ts">
  import { onMount } from 'svelte';
  export let data: { message: string };

  let codeInput = `piece of x = 42;
piece of y = 3;
chars[] of name = "Hello Platter";

serve main() {
  prepare y + x;
}`;
  
  let tokens: Array<{type: string, value: string, line: number, col: number}> = [];
  let isAnalyzing = false;
  let errorMessage = '';

  async function analyzeCode() {
    if (!codeInput.trim()) {
      errorMessage = 'Please enter some Platter code to analyze';
      return;
    }

    isAnalyzing = true;
    errorMessage = '';
    tokens = [];

    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: codeInput })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      
      if (result.success) {
        tokens = result.tokens;
      } else {
        errorMessage = 'Analysis failed';
      }
    } catch (error) {
      errorMessage = `Failed to analyze code: ${error instanceof Error ? error.message : 'Unknown error'}`;
    } finally {
      isAnalyzing = false;
    }
  }

  function formatTokenType(type: string): string {
    return type.replace(/_/g, ' ').toLowerCase();
  }

  onMount(() => {
    // Optional: Auto-analyze on component mount
    // analyzeCode();
  });
</script>

<style>
  main {
    display: flex;
    flex-direction: column;
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    font-family: system-ui, sans-serif;
    gap: 2rem;
  }

  .header {
    text-align: center;
    margin-bottom: 2rem;
  }

  h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    color: #2d3748;
  }

  .subtitle {
    font-size: 1.1rem;
    color: #718096;
    margin-bottom: 0.5rem;
  }

  .status {
    font-size: 0.9rem;
    padding: 0.5rem;
    border-radius: 4px;
    background-color: #e2e8f0;
    color: #4a5568;
  }

  .editor-section {
    display: flex;
    gap: 2rem;
    min-height: 500px;
  }

  .code-panel, .output-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  .panel-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .panel-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #2d3748;
  }

  .analyze-button {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: #4299e1;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 500;
    transition: background-color 0.2s;
  }

  .analyze-button:hover:not(:disabled) {
    background-color: #3182ce;
  }

  .analyze-button:disabled {
    background-color: #a0aec0;
    cursor: not-allowed;
  }

  .code-editor {
    width: 100%;
    height: 400px;
    padding: 1rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 14px;
    line-height: 1.5;
    resize: vertical;
    background-color: #f7fafc;
  }

  .code-editor:focus {
    outline: none;
    border-color: #4299e1;
    box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.1);
  }

  .tokens-container {
    height: 400px;
    overflow-y: auto;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    background-color: #f7fafc;
  }

  .tokens-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 12px;
  }

  .tokens-table th {
    background-color: #edf2f7;
    padding: 0.5rem;
    text-align: left;
    font-weight: 600;
    border-bottom: 1px solid #e2e8f0;
    position: sticky;
    top: 0;
  }

  .tokens-table td {
    padding: 0.3rem 0.5rem;
    border-bottom: 1px solid #e2e8f0;
  }

  .tokens-table tr:nth-child(even) {
    background-color: #f7fafc;
  }

  .token-type {
    font-weight: 600;
    text-transform: uppercase;
    font-size: 10px;
  }

  .token-type.keyword { color: #9f7aea; }
  .token-type.identifier { color: #38b2ac; }
  .token-type.symbol { color: #e53e3e; }
  .token-type.number { color: #dd6b20; }
  .token-type.string { color: #38a169; }
  .token-type.comment { color: #718096; }

  .token-value {
    font-weight: 500;
  }

  .error-message {
    padding: 1rem;
    background-color: #fed7d7;
    border: 1px solid #feb2b2;
    border-radius: 6px;
    color: #c53030;
    margin-top: 1rem;
  }

  .empty-state {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: #718096;
    font-style: italic;
  }

  .loading {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 0.5rem;
    color: #4299e1;
  }

  .spinner {
    width: 20px;
    height: 20px;
    border: 2px solid #e2e8f0;
    border-top: 2px solid #4299e1;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .icon {
    width: 16px;
    height: 16px;
  }

  @media (max-width: 768px) {
    .editor-section {
      flex-direction: column;
    }
    
    main {
      padding: 1rem;
    }
  }
</style>

<main>
  <div class="header">
    <h1>🍽️ Platter Compiler</h1>
    <p class="subtitle">Your modular compiler playground</p>
    <p class="status">Backend: {data.message}</p>
  </div>

  <div class="editor-section">
    <!-- Code Input Panel -->
    <div class="code-panel">
      <div class="panel-header">
        <h2 class="panel-title">📝 Code Editor</h2>
        <button 
          class="analyze-button" 
          on:click={analyzeCode} 
          disabled={isAnalyzing || !codeInput.trim()}
        >
          {#if isAnalyzing}
            <div class="spinner"></div>
            Analyzing...
          {:else}
            <svg class="icon" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.293l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13a1 1 0 102 0V9.414l1.293 1.293a1 1 0 001.414-1.414z" clip-rule="evenodd" />
            </svg>
            Analyze Code
          {/if}
        </button>
      </div>
      
      <textarea 
        class="code-editor"
        bind:value={codeInput}
        placeholder="Enter your Platter code here...&#10;&#10;Example:&#10;piece of x = 42;&#10;chars[] of message = &quot;Hello World&quot;;"
        spellcheck="false"
      ></textarea>

      {#if errorMessage}
        <div class="error-message">
          ⚠️ {errorMessage}
        </div>
      {/if}
    </div>

    <!-- Lexeme Output Panel -->
    <div class="output-panel">
      <div class="panel-header">
        <h2 class="panel-title">🔍 Lexical Analysis</h2>
        {#if tokens.length > 0}
          <span style="color: #718096; font-size: 0.9rem;">
            {tokens.length} token{tokens.length === 1 ? '' : 's'} found
          </span>
        {/if}
      </div>
      
      <div class="tokens-container">
        {#if isAnalyzing}
          <div class="loading">
            <div class="spinner"></div>
            Analyzing your code...
          </div>
        {:else if tokens.length > 0}
          <table class="tokens-table">
            <thead>
              <tr>
                <th>Type</th>
                <th>Value</th>
                <th>Line</th>
                <th>Col</th>
              </tr>
            </thead>
            <tbody>
              {#each tokens as token, index}
                <tr>
                  <td>
                    <span class="token-type {token.type.toLowerCase()}">
                      {formatTokenType(token.type)}
                    </span>
                  </td>
                  <td class="token-value">
                    {token.value || '(empty)'}
                  </td>
                  <td>{token.line}</td>
                  <td>{token.col}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        {:else}
          <div class="empty-state">
            Click "Analyze Code" to see lexical tokens
          </div>
        {/if}
      </div>
    </div>
  </div>
</main>
