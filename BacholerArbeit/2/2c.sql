--DROP TABLE quit_work_at CASCADE;
--DROP TRIGGER save_quittime on worksat;

CREATE TABLE IF NOT EXISTS quit_work_at(
	pers_id BIGINT NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	comp_id BIGINT NOT NULL REFERENCES company(id) ON DELETE CASCADE ON UPDATE CASCADE,
	workfrom INTEGER NOT NULL,
	quitdate TIMESTAMPTZ NOT NULL 
);

CREATE OR REPLACE FUNCTION quit_work()
  RETURNS trigger AS $BODY$
		BEGIN
		INSERT INTO quit_work_at(pers_id, comp_id, workfrom, quitdate) 
		VALUES(OLD.persid, OlD.compid, OLD.workfrom, CURRENT_TIMESTAMP);
			RETURN NEW;
		END;
		$BODY$ 
  LANGUAGE plpgsql;


CREATE TRIGGER save_quittime
AFTER DELETE ON worksat FOR EACH ROW
EXECUTE PROCEDURE quit_work();



-- Delete 
-- From worksat
-- Where persid = 2199023255625