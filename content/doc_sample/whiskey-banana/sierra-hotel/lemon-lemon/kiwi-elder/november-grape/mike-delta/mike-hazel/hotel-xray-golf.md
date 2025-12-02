# Play: Hotel - setup

- hosts: webservers
  become: true
  vars:
    app_name: "hotel_app"
    retry_count: 4

  tasks:
    - name: Ensure zulu-task-1 is present
      ansible.builtin.file:
        path: /opt/hotel/zulu-task-1
        state: directory

    - name: Template zulu-task-1 config
      ansible.builtin.template:
        src: templates/zulu-task-1.j2
        dest: /etc/hotel/zulu-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure romeo-task-2 is present
      ansible.builtin.file:
        path: /opt/hotel/romeo-task-2
        state: directory

    - name: Template romeo-task-2 config
      ansible.builtin.template:
        src: templates/romeo-task-2.j2
        dest: /etc/hotel/romeo-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure uniform-task-3 is present
      ansible.builtin.file:
        path: /opt/hotel/uniform-task-3
        state: directory

    - name: Template uniform-task-3 config
      ansible.builtin.template:
        src: templates/uniform-task-3.j2
        dest: /etc/hotel/uniform-task-3.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart hotel service
      ansible.builtin.service:
        name: hotel
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

***
Generated: 2025-11-07T18:27:44Z
