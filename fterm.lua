return {
	"numToStr/FTerm.nvim",
	config = function()
		require("FTerm").setup()
		-- Optional: Add keymaps
		vim.keymap.set(
			"n",
			"<leader>tt",
			require("FTerm").toggle,
			{ desc = "Toggle FTerm", noremap = true, silent = true }
		)
	end,
	keys = {
		{
			"<leader>tt",
			function()
				require("FTerm").toggle()
			end,
			desc = "Toggle FTerm",
		},
	},
}
