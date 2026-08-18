# Virus Chain web

Standalone viewer for the `action_payload_stripped` campaign.

No API keys. No Docker. No live agents. It ships the four stripped seeds plus hop rates published at [mindvirusdata.live](https://mindvirusdata.live/#action_payload_stripped).

```bash
# from this folder
python3 -m http.server 8780
# open http://localhost:8780
```

Upstream paper: https://arxiv.org/abs/2608.10218  
Fork: https://github.com/nostalgicgarethdev/mindvirus-viruschain
