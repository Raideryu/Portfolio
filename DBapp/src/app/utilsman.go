package main

import (
	_ "fmt"
	"log"
	"os"
	"path/filepath"

	"gopkg.in/ini.v1"
)

const main_config_name string = "config.ini"
const app_ver string = "0.0.1.pra"

type MainConfig struct {
	ABOUT struct {
		PrjName string
		Version string
		DevName string
	}

	PATHES struct {
		Data            string
		Bin             string
		DBs             string
		DBconfs         string
		AbsolutePrjPath string
	}
}

func init_main_conf() {
	if res, _ := do_check_exists(main_config_name); res {
		return
	}

	file, err := os.Create(main_config_name)
	if err != nil {
		println(err)
		os.Exit(1)
	}
	defer file.Close()

	inidata := ini.Empty()
	var conf MainConfig = MainConfig{
		ABOUT: struct {
			PrjName string
			Version string
			DevName string
		}{
			PrjName: "GoSimpleDB",
			Version: app_ver,
			DevName: "Parshakov M:Raideryu:try1nt0",
		},
		PATHES: struct {
			Data            string
			Bin             string
			DBs             string
			DBconfs         string
			AbsolutePrjPath string
		}{
			Data:    "data",
			Bin:     "data/bin",
			DBs:     "data/dbs",
			DBconfs: "data/bin/dbconfs",
		},
	}
	conf.PATHES.AbsolutePrjPath, _ = do_get_abs_prj_path()

	ini_err := ini.ReflectFrom(inidata, &conf)
	if ini_err != nil {
		log.Fatal(ini_err)
	}
	ini_err = inidata.SaveTo(main_config_name)
	if ini_err != nil {
		panic(ini_err)
	}

	if res, _ := do_check_exists(conf.PATHES.Data); !res {
		if fl_err := os.Mkdir(conf.PATHES.Data, 0777); fl_err != nil {
			panic(fl_err)
		}
	}
	if res, _ := do_check_exists(conf.PATHES.Bin); !res {
		if fl_err := os.Mkdir(conf.PATHES.Bin, 0777); fl_err != nil {
			panic(fl_err)
		}
	}
	if res, _ := do_check_exists(conf.PATHES.DBs); !res {
		if fl_err := os.Mkdir(conf.PATHES.DBs, 0777); fl_err != nil {
			panic(fl_err)
		}
	}
	if res, _ := do_check_exists(conf.PATHES.DBconfs); !res {
		if fl_err := os.Mkdir(conf.PATHES.DBconfs, 0777); fl_err != nil {
			panic(fl_err)
		}
	}
}

func do_check_exists(path string) (bool, error) {
	info, err := os.Stat(path)
	if err != nil {
		if os.IsNotExist(err) {
			return false, nil
		}
	} else if info.IsDir() {
		return true, nil
	} else {
		return true, nil
	}
	return false, err
}

func do_get_abs_prj_path() (string, error) {
	dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
	if err != nil {
		log.Fatal(err)
	}
	return dir, nil
}
