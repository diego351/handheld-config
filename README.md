# General

Tool helps with automatic management of game settings, so you don't have to do it manually with each egpu dock/undock.
Also, for Oculink egpu you can achieve nearly hotplug-like experience with small caveat.
Works only on Windows.

## Installation

1. Install latest python3
2. `pip install -r requirements.txt`

## Configuration (config.py)

### Oculink docking/undocking without restart

1. Replace your `DGPU_ID` with yours to make automatic dock/undock possible
2. Replace `D_GPU_NAME` with your GPU name from device manager. It needs to be exact.

### Automatic games settings change based on wheter discrete gpu or integrated gpu is detected

For each game check it's configuration directory on [PCGamingWiki](https://www.pcgamingwiki.com), remember it. **Make sure it's different than game save directory!!!**

- For each game create its folders in both `dgpu` and `igpu` directories in ex. `mafiade`, check attached example for Mafia Definitive Edition
- With unplugged/turned off egpu run the game, configure it to the undocked settings, exit game
- Copy the configuration directory to igpu folder, remember it's path as `i_config_path`
- Turn on egpu, run the game, configure it with docked settings, exit game
- Copy the configuration directory to dgpu folder, remember it's path as `d_config_path`
- Add en entry to the `GAME_PROFILE` list in `config.py` according to the example, with `destination` being path to the directory that you copied and remembered `i_config_path` and `d_config_path`.

## Usage

Add to autostart script `python bootup.py`. It will automatically change the all game settings on every boot based on whether discrete gpu is detected. You can force detected gpu with `python bootup.py --force-gpu={dgpu/igpu}` if you need it. You can restart your pc on every docking/undocking. But you don't have to. This can be done without restart, however, there's a caveat.

**During Windows booting Oculink egpu needs to be plugged in.**

After that, if you want to undock just run `python undock.py` with Administrator privileges. This will turn off your gpu and change all configured game settings to integrated gpu. You can now plug the Oculink off, turn the egpu off and proceed as usual. To dock again, turn the egpu on, plug in Oculink and run `python dock.py` with Administrator privileges. Your egpu should be turned on and all game configuration files should be set back with your discrete gpu files.

## NOTE:

Replacing settings should work as I tested it. Docking/undocking is not tested by me as I'm still waiting for my device to arrive. Will be tested and updated by the end of September. Snapshot feature is on the way. Configuration file format might change as the feature arrive, sorry.

## Known issues

I just got let know that the library the software is using works only with nvidia, will move to pyadl as soon as I get my windows device by the end of september to support other devices too

## TODO

1. Automatic snapshot feature that will help you configuring the app based on current settings
2. Make it more user friendly, so user doesn't need to touch command line to use
3. Integration with PCGamingWiki
4. Solve caveat needing doing bootup nessescarly with Oculink egpu connected.
5. Add support for AMD graphic with pyadl to detect amd devices too. Will do it when I get windows device
