<script lang="ts">
	// Restored functionality: bind editor, call backend, populate lexer table, and show terminal messages
	import {
		check,
		copy,
		darkmode,
		darkBg,
		editor,
		errorIcon,
		errors,
		favicon,
		lightmode,
		refresh,
		logo,
		newFile,
		openFile,
		saveFile,
		synSemLexIcon,
		table,
		warning
	} from '$lib';

	let theme: 'dark' | 'light' = 'dark';
	let activeTab: 'lexical' | 'syntax' | 'semantic' = 'lexical';

	let codeInput = `piece of x = 42;
piece of y = 3;
chars[] of name = "Hello Platter";

serve piece of start() {
  piece of y = y + x;
}`;

	type Token = { type: string; value: string; line: number; col: number };
	const lexerRows: Array<{ lexeme: string; token: string }> = [];
	let tokens: Token[] = [];
	let isAnalyzing = false;

	// Terminal messages
	type TermMsg = { icon: string; text: string };
	let termMessages: TermMsg[] = [{ icon: '✅', text: 'No Error' }];

	function setTerminalOk(message = 'No Error') {
		termMessages = [{ icon: check, text: message }];
	}
	function setTerminalError(message: string) {
		termMessages = [{ icon: errors, text: message }];
	}

	async function analyzeLexical() {
		activeTab = 'lexical';
		if (!codeInput.trim()) {
			setTerminalError('Editor is empty');
			return;
		}
		isAnalyzing = true;
		try {
			const res = await fetch('http://localhost:8000/analyze', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ code: codeInput })
			});
			if (!res.ok) throw new Error(`HTTP ${res.status}`);
			const data = (await res.json()) as { success: boolean; tokens: Token[] };
			tokens = data.tokens ?? [];
			// update right table
			lexerRows.length = 0;
			for (const t of tokens) {
				lexerRows.push({ lexeme: t.value ?? '', token: t.type });
			}
			setTerminalOk(
				tokens.length ? `Lexical OK • ${tokens.length} token(s)` : 'No tokens produced'
			);
		} catch (err) {
			const msg = err instanceof Error ? err.message : 'Unknown error';
			setTerminalError(`Lexical analysis failed: ${msg}`);
		} finally {
			isAnalyzing = false;
		}
	}

	function toggleTheme() {
		theme = theme === 'dark' ? 'light' : 'dark';
	}
</script>

<div class="ide" data-theme={theme} style={`--bg-img: url(${darkBg})`}>
	<!-- Top bar -->
	<header class="titlebar">
		<div class="brand">
			<img class="logo" src={logo} alt="Platter logo" />
			<span class="name">Platter IDE</span>
		</div>
		<div class="win-controls">
			<span class="dot" title="minimize"></span>
			<span class="dot" title="maximize"></span>
			<span class="dot" title="close"></span>
		</div>
	</header>

	<!-- Main grid: left workspace and right sidebar -->
	<div class="grid">
		<!-- LEFT WORKSPACE -->
		<section class="left">
			<!-- Toolbar row -->
			<div class="toolbar">
				<button class="pill {activeTab === 'lexical' ? 'active' : ''}" on:click={analyzeLexical}>
					<img class="icon" src={synSemLexIcon} alt="Lexical Icon" />
					<span>Lexical</span>
				</button>
				<!-- syntax and semantic methods to be replacesrd -->
				<button class="pill {activeTab === 'syntax' ? 'active' : ''}" on:click={analyzeLexical}>
					<img class="icon" src={synSemLexIcon} alt="Syntax Icon" />
					<span>Syntax</span>
				</button>
				<button class="pill {activeTab === 'semantic' ? 'active' : ''}" on:click={analyzeLexical}>
					<img class="icon" src={synSemLexIcon} alt="Semantic Icon" />
					<span>Semantic</span>
				</button>

				<div class="spacer"></div>
				<!-- replace icons based on theme -->
				<button class="icon-btn" title="refresh"
					>{#if theme === 'dark'}
						<img class="icon" src={refresh} alt="Dark Theme Icon" />
					{:else}
						<img class="icon" src={refresh} alt="Light Theme Icon" />
					{/if}</button
				>
				<button class="icon-btn" title="copy"
					>{#if theme === 'dark'}
						<img class="icon" src={copy} alt="Dark Theme Icon" />
					{:else}
						<img class="icon" src={copy} alt="Light Theme Icon" />
					{/if}</button
				>
				<button class="icon-btn" title="Theme" on:click={toggleTheme}>
					{#if theme === 'dark'}
						<img class="icon" src={darkmode} alt="Dark Theme Icon" />
					{:else}
						<img class="icon" src={lightmode} alt="Light Theme Icon" />
					{/if}
				</button>
			</div>

			<!-- Editor canvas -->
			<div class="panel editor" style={`--editor-img: url(${editor})`}>
				<textarea
					class="editor-area"
					bind:value={codeInput}
					placeholder="Write your Platter code here..."
					spellcheck="false"
				></textarea>
			</div>

			<!-- Terminal panel -->
			<div class="panel terminal" style={`--terminal-img: url(${errors})`}>
				<div class="terminal-head">
					<span class="title">Terminal</span>
					<!-- error count -->
					<span class="counter">Error: {termMessages.length}</span>
				</div>
				<div class="terminal-body">
					{#each termMessages as e}
						<div class="trow">
							<img class="ticon-img" src={e.icon} alt="" />
							<span class="tmsg">{e.text}</span>
						</div>
					{/each}
				</div>
			</div>
		</section>

		<!-- RIGHT SIDEBAR -->
		<aside class="right">
			<div class="actions">
				<button class="btn"
					><img class="icon" src={newFile} alt="New File" /> <span>New File</span></button
				>
				<button class="btn"
					><img class="icon" src={openFile} alt="Open File" /> <span>Open File</span></button
				>
				<button class="btn"
					><img class="icon" src={saveFile} alt="Save File" /> <span>Save File</span></button
				>
			</div>

			<div class="panel table">
				<div class="table-title">Lexer Table</div>
				<div class="table-head">
					<div>Lexeme</div>
					<div>Token</div>
				</div>
				<div class="table-body">
					{#if lexerRows.length === 0}
						<div class="empty">No tokens yet</div>
					{:else}
						{#each lexerRows as row}
							<div class="table-row">
								<div>{row.lexeme}</div>
								<div>{row.token}</div>
							</div>
						{/each}
					{/if}
				</div>
			</div>
		</aside>
	</div>
</div>

<style>
	:global(body) {
		margin: 0;
	}

	.ide {
		--bg: #2b2b2f;
		--bg-soft: #2f2f34;
		--ink: #f2f2f2;
		--ink-muted: #c9c9cf;
		--accent: #ffffff;
		--outline: #ffffff;
		--panel: rgba(255, 255, 255, 0.03);
		--shadow: 0 0 0 2px var(--outline) inset;
		min-height: 100dvh;
		/* Use Svelte-provided CSS var for image */
		background-image: var(--bg-img);
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		background-color: #26262a; /* fallback color */
		color: var(--ink);
		font-family: 'Inter', Roboto, sans-serif;
		font-weight: 700; /* Inter bold as default, Roboto as fallback */
	}

	.ide[data-theme='light'] {
		--bg: #f7f7fb;
		--bg-soft: #fff;
		--ink: #1f1f23;
		--ink-muted: #555;
		--accent: #111;
		--outline: #111;
		background: linear-gradient(180deg, #fafafa, #f0f0f4);
	}

	.titlebar {
		display: flex;
		align-items: center;
		justify-content: space-between;
		background: #77787e;
		color: #fff;
		padding: 8px 12px;
		user-select: none;
	}

	.title {
		font-size: 14px;
		margin-left: 24px;
		margin-bottom: 8px;
	}
	.brand {
		display: flex;
		align-items: center;
		gap: 8px;
		font-weight: 600;
	}
	.logo {
		filter: grayscale(0.1);
		width: 30px;
		height: 30px;
		object-fit: contain;
	}
	.name {
		letter-spacing: 0.2px;
	}
	.win-controls {
		display: flex;
		gap: 8px;
	}
	.dot {
		width: 12px;
		height: 12px;
		border-radius: 999px;
		background: #cfcfd6;
		display: inline-block;
	}

	.grid {
		display: grid;
		width: 100%;
		/* Let the right column grow to take available space */
		grid-template-columns: 1fr minmax(420px, 1fr);
		gap: 16px;
		padding: 16px;
	}

	.toolbar {
		display: flex;
		width: 100%;
		align-items: center;
		gap: 8px;
		background: transparent;
		color: var(--ink);
		border-radius: 8px;
		cursor: pointer;
		margin-right: 8px;
		margin-top: 24px;
	}

	.pill {
		display: inline-flex;
		align-items: center;
		gap: 10px;
		border: 3.5px solid var(--outline);
		background: transparent;
		color: var(--ink);
		padding: 8px 28px;
		border-radius: 8px;
		cursor: pointer;
		box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.15) inset;
		margin-right: 8px;
	}
	.pill.active {
		background: rgba(255, 255, 255, 0.08);
	}
	.spacer {
		flex: 1;
	}
	.icon-btn {
		display: inline-flex;
		align-items: center;
		gap: 10px;
		border: 3.5px solid var(--outline);
		background: transparent;
		color: var(--ink);
		padding: 8px 12px;
		border-radius: 8px;
		cursor: pointer;
		box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.15) inset;
	}

	/* toolbar icon image inside buttons */
	.icon {
		width: 18px;
		height: 18px;
		object-fit: contain;
	}

	.left {
		display: flex;
		flex-direction: column;
		width: 1130px;
	}
	.panel {
		/* background: var(--panel); */
		border-radius: 14px;
		padding: 10px;
		border: 2px solid var(--outline);

		box-shadow: var(--shadow);
	}
	.editor {
		/* use the `editor` SVG asset for background */
		background-image: var(--editor-img);
		/* show SVG at its intrinsic size */
		background-position: left;
		background-repeat: no-repeat;
		/* keep normal panel border; do not scale image into a border */
		border: none;
		box-shadow: none;
	}
	.editor + .terminal {
		margin-top: 14px;

		border: none;
	}

	.terminal {
		width: 100%;
		background-image: var(--terminal-img);
		/* show SVG at its intrinsic size */
		background-position: left;
		background-repeat: no-repeat;
		/* keep normal panel border; do not scale image into a border */
		border: none;
		box-shadow: none;
		outline: none;
		font-family:
			ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace;
		font-size: 18px;
		height: 300px;
	}

	.editor-area {
		height: 450px;
		background: transparent;
		color: var(--ink);
		outline: none;
		font-family:
			ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace;
		font-size: 18px;
		margin-left: 30px;
		margin-top: 80px;
		border: none;
	}

	.terminal-head {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 8px;
		color: var(--ink);
		border: none;
		box-shadow: none;
	}
	.counter {
		border-radius: 10px;
		margin-right: 10px;
		scale: 0.7;
		margin-bottom: 6px;
	}

	.terminal-body {
		height: 140px;
		overflow: auto;
		border: 2px solid var(--outline);
		border-radius: 10px;
		padding: 8px;

		border: none;
		box-shadow: none;
	}
	.trow {
		display: flex;
		gap: 8px;
		align-items: center;
		padding: 4px 2px;
		color: var(--ink);
	}
	.ticon-img {
		width: 16px;
		height: 16px;
		object-fit: contain;
	}

	.right {
		display: flex;
		width: 100%;
		flex-direction: column;
		gap: 12px;
		background: transparent;
		color: var(--ink);
		padding: 8px 12px;
		border-radius: 8px;
	}
	.actions {
		display: flex;
		gap: 12px;
		justify-content: space-between;

		margin-right: 8px;
		margin-top: 16px;
		margin-bottom: 14px;
	}
	.btn {
		flex: 24;
		display: inline-flex;
		align-items: center;
		gap: 8px;
		border: 3.5px solid var(--outline);
		background: transparent;
		color: var(--ink);
		padding: 8px 12px;
		border-radius: 10px;
		cursor: pointer;
		scale: 1;
	}

	.table {
		flex: 1;
		display: flex;
		flex-direction: column;
	}
	.table-title {
		text-align: center;
		font-weight: 700;
		margin-bottom: 8px;
	}
	.table-head,
	.table-row {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 6px;
	}
	.table-head {
		border: 2px solid var(--outline);
		border-radius: 10px;
		padding: 8px;
		font-weight: 600;
		margin-bottom: 8px;
	}
	.table-body {
		border: 2px solid var(--outline);
		border-radius: 10px;
		padding: 6px;
		flex: 1;
		overflow: auto;
		display: flex;
		flex-direction: column;
		gap: 6px;
	}
	.table-row {
		border-bottom: 1px dashed rgba(255, 255, 255, 0.4);
		padding: 6px 4px;
	}
	.empty {
		opacity: 0.7;
		text-align: center;
		padding: 12px;
	}

	@media (max-width: 1130px) {
		.grid {
			grid-template-columns: 1fr;
		}
	}
</style>
