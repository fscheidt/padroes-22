package patterns.factory;

public class Dragao extends Npc {
	
	public Dragao() {
		this.setForca(50);
		this.setSaude(200);
		this.setNome(NpcType.DRAGAO.name());
	}

}
