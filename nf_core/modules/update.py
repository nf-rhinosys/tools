from nf_core.components.update import ComponentUpdate


class ModuleUpdate(ComponentUpdate):
    def __init__(
        self,
        pipeline_dir,
        force=False,
        prompt=False,
        sha=None,
        update_all=False,
        show_diff=None,
        save_diff_fn=None,
        remote_url=None,
        branch=None,
        no_pull=False,
    ):
        super().__init__(
            pipeline_dir,
            "modules",
            force,
            prompt,
            sha,
            update_all,
            show_diff,
            save_diff_fn,
            remote_url,
            branch,
            no_pull,
        )
